from langchain.tools import tool
from src.constants import get_price_list
from langchain.tools import tool


@tool
def estimate_cart(cart_items: list):
    """
    Calculate final estimate including visit charge and tax.
    cart_items format:
    [
      { "code": "FAN_REPAIR", "quantity": 2 }
    ]
    """
    price_data = get_price_list()
    rules = price_data["pricing_rules"]

    subtotal = 0
    breakdown = []

    # Flatten all services into a lookup table
    service_lookup = {}
    for key, section in price_data.items():
        if key == "pricing_rules":
            continue
        for item in section["items"]:
            service_lookup[item["code"]] = item

    for item in cart_items:
        service = service_lookup.get(item["code"])
        if not service:
            continue

        price = service["base_price"] * item["quantity"]
        subtotal += price

        breakdown.append({
            "code": service["code"],
            "name": service["name"],
            "quantity": item["quantity"],
            "unit_price": service["base_price"],
            "total_price": price
        })

    visit_charge = rules["minimum_visit_charge"]
    tax = (subtotal + visit_charge) * rules["tax_percentage"] / 100
    total = subtotal + visit_charge + tax

    return {
        "items": breakdown,
        "subtotal": subtotal,
        "visit_charge": visit_charge,
        "tax": round(tax, 2),
        "total": round(total, 2)
    }


@tool
def search_service(query: str | None = None):
    """
    Search available electrician services.
    If query is provided, filters services by name or category.
    """
    price_data = get_price_list()
    results = []

    for key, section in price_data.items():
        # Skip pricing rules
        if key == "pricing_rules":
            continue

        category_name = section.get("category")
        items = section.get("items", [])

        matched_items = []

        for item in items:
            if not query:
                matched_items.append({
                    "code": item["code"],
                    "name": item["name"],
                    "unit": item["unit"],
                    "description": item["description"]
                })
            else:
                q = query.lower()
                if (
                    q in item["name"].lower()
                    or q in item["description"].lower()
                    or q in category_name.lower()
                ):
                    matched_items.append({
                        "code": item["code"],
                        "name": item["name"],
                        "unit": item["unit"],
                        "description": item["description"]
                    })

        if matched_items:
            results.append({
                "category": category_name,
                "items": matched_items
            })

    return {
        "service": "Electrician",
        "results": results
    }


@tool
def get_price(code: str, quantity: int = 1):
    """
    Get price for a specific service code and quantity.
    """
    if quantity <= 0:
        return {
            "error": "Quantity must be greater than zero"
        }

    price_data = get_price_list()

    # Build lookup table
    service_lookup = {}
    for key, section in price_data.items():
        if key == "pricing_rules":
            continue
        for item in section.get("items", []):
            service_lookup[item["code"]] = item

    service = service_lookup.get(code)

    if not service:
        return {
            "error": f"Service code '{code}' not found"
        }

    unit_price = service["base_price"]
    total_price = unit_price * quantity

    return {
        "code": service["code"],
        "name": service["name"],
        "unit": service["unit"],
        "unit_price": unit_price,
        "quantity": quantity,
        "total_price": total_price
    }


@tool
def add_to_cart(cart: list, code: str, quantity: int):
    """
    Add or update a service in the cart.

    cart format:
    [
      {"code": "FAN_REPAIR", "quantity": 2}
    ]
    """
    if quantity <= 0:
        return {
            "error": "Quantity must be greater than zero"
        }

    # Validate service code exists
    price_data = get_price_list()
    valid_codes = set()

    for key, section in price_data.items():
        if key == "pricing_rules":
            continue
        for item in section.get("items", []):
            valid_codes.add(item["code"])

    if code not in valid_codes:
        return {
            "error": f"Invalid service code: {code}"
        }

    # Merge or add item
    updated = False
    for item in cart:
        if item["code"] == code:
            item["quantity"] += quantity
            updated = True
            break

    if not updated:
        cart.append({
            "code": code,
            "quantity": quantity
        })

    return {
        "message": "Item added to cart",
        "cart": cart
    }
