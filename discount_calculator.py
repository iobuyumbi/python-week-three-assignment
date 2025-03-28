def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    :param price: Original price of the item
    :param discount_percent: Discount percentage
    :return: Final price after applying discount (if applicable)
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        final_price = price
        return final_price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate and print the final price
final_price = calculate_discount(original_price, discount_percentage)
print(f"Final price: {final_price:.2f}")