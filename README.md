## Order Status Values:
### class OrderStatus(str, Enum):
    PENDING = "pending"              # Just created
    CONFIRMED = "confirmed"          # Admin/System confirmed
    PROFESSIONAL_ASSIGNED = "professional_assigned"  # Professional assigned
    IN_PROGRESS = "in_progress"      # Professional is working
    COMPLETED = "completed"          # Work finished
    CANCELLED = "cancelled"          # Cancelled by user/admin
    FAILED = "failed"                # Something went wrong


## Payment Status Values:
### class PaymentStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"
    REFUNDED = "refunded"


## Booking Page:

Displays All Order Information:

- Order number & date
- Status badge with color coding (Pending, Confirmed, In Progress, Completed, etc.)
- All services with icons and quantities
- Schedule info (Today/Tomorrow/Date + Time)
- Professional details (photo, name, rating)
- Address
- Total amount
- View Details button

## ✅ Status Colors:

🟡 Pending - Orange
🔵 Confirmed - Blue
🟣 Professional Assigned - Purple
🔵 In Progress - Cyan
🟢 Completed - Green
🔴 Cancelled/Failed - Red

## ✅ Additional Features:

- Pull to refresh
- Empty state with "Browse Services" button
- Loading indicator
- Matches your app's design system

