# Discount Calculator Program

def calculate_discount(price, discount_percent):
    """
    Calculates final price after discount.
    Applies discount only if discount_percent is 20% or higher.
    Otherwise returns original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Main program
def main():
    print("=== Discount Calculator ===")
    
    try:
        # Get user input
        original_price = float(input("Enter the original price of the item: $"))
        discount_percentage = float(input("Enter the discount percentage: "))
        
        # Input validation
        if original_price < 0 or discount_percentage < 0:
            print("Error: Price and discount percentage cannot be negative.")
            return
        
        # Calculate final price
        final_price = calculate_discount(original_price, discount_percentage)
        
        # Display results
        print("\n=== Results ===")
        if discount_percentage >= 20:
            print(f"Original price: ${original_price:.2f}")
            print(f"Discount applied: {discount_percentage}%")
            print(f"Discount amount: ${original_price * (discount_percentage / 100):.2f}")
            print(f"Final price after discount: ${final_price:.2f}")
        else:
            print(f"No discount applied (needs 20% or higher)")
            print(f"Final price: ${final_price:.2f}")
            
    except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage.")

# Run the program
if __name__ == "__main__":
    main()