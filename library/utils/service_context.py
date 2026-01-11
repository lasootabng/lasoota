from src.constants import get_price_list

def build_service_context() -> str:
    price_data = get_price_list()
    lines = []

    for key, section in price_data.items():
        if key == "pricing_rules":
            continue

        for item in section["items"]:
            lines.append(
                f"- Code: {item['code']}, "
                f"Name: {item['name']}, "
                f"Description: {item['description']}"
            )

    return "\n".join(lines)
