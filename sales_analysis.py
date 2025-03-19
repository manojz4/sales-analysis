# Sample sales data
sales_data = {
    'January': 1500,
    'February': 2400,
    'March': 3200,
    'April': 800,
    'May': 1900,
    'June': 2200,
}

# Threshold for good performance
good_performance_threshold = 2000

# Iterate over sales data using loops
for month, sales in sales_data.items():
    # Using conditions to categorize sales performance
    if sales > good_performance_threshold:
        print(f"{month}: Good sales performance - ${sales}")
    elif sales == good_performance_threshold:
        print(f"{month}: Average sales performance - ${sales}")
    else:
        print(f"{month}: Needs improvement - ${sales}")
