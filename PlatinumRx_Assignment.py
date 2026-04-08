
# SQL PROFICIENCY SOLUTIONS

"""
-- A. Hotel Management System --

1. User ID and last booked room:
SELECT user_id, room_no
FROM (
    SELECT user_id, room_no, 
           ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY booking_date DESC) as rn
    FROM bookings
) t WHERE rn = 1;

2. Booking ID and total billing for Nov 2021:
SELECT b.booking_id, SUM(bc.item_quantity * i.item_rate) as total_billing
FROM bookings b
JOIN booking_commercials bc ON b.booking_id = bc.booking_id
JOIN items i ON bc.item_id = i.item_id
WHERE b.booking_date BETWEEN '2021-11-01' AND '2021-11-30'
GROUP BY b.booking_id;

3. Bills > 1000 in Oct 2021:
SELECT bill_id, SUM(item_quantity * item_rate) as total
FROM booking_commercials bc
JOIN items i ON bc.item_id = i.item_id
WHERE bill_date BETWEEN '2021-10-01' AND '2021-10-31'
GROUP BY bill_id HAVING total > 1000;

-- B. Clinic Management System --

1. Revenue per sales channel (2021):
SELECT sales_channel, SUM(amount) FROM clinic_sales 
WHERE EXTRACT(YEAR FROM datetime) = 2021 GROUP BY 1;
"""


# PYTHON PROFICIENCY SOLUTIONS


def convert_minutes(n):
    """Task 1: Minutes to Human Readable Form"""
    hours = n // 60
    minutes = n % 60
    return f"{hours}hr {minutes}minutes" if hours > 0 else f"{minutes}minutes"

def remove_duplicates(s):
    """Task 2: Remove duplicates using a loop"""
    unique_str = ""
    for char in s:
        if char not in unique_str:
            unique_str += char
    return unique_str

# Testing Python Tasks
if __name__ == "__main__":
    print(f"130 minutes -> {convert_minutes(130)}")
    print(f"Duplicate removal ('platinumrx') -> {remove_duplicates('platinumrx')}")


# SPREADSHEET SOLUTIONS (Logic)

"""
1. VLOOKUP for 'ticket_created_at': 
   =VLOOKUP(E2, ticket_sheet!$A$2:$B$100, 2, FALSE)
   (Assumes CMS_ID is the common key)

2. Count tickets created/closed same day:
   Use COUNTIFS or a Pivot Table with a helper column:
   =IF(INT(created_at) = INT(closed_at), "Same Day", "Different Day")
"""
