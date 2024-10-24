from time import sleep # Doesn't really make a difference, just tells anyone reading the code what methods you're using from the library.

def gbp_to_usd(gbp_amount):
    return gbp_amount * 0.5,"$" # I don't know the maths to convert to yen.

# Then make other methods similar to that for each currency.

def main():
    # Not gonna lie, I would be lazy and just use a try except to get around having to error-proof these inputs, but you're not smart enough for that.
    gbp_inp = float(input(f"Enter the money you'd like to convert.\n £"))
    convert_to = str(input(f"What would you like to convert your £{gbp_inp:.2f} into?\n- USD\n\nOr press RETURN to change your money amount."))

    if convert_to == "":
        main()

    gbp_converted = None # This is where the variable is created so that I can access it outside of the match case. No need for all that global stuff.
    converted_symbol = None
    match str.lower(convert_to):
        case "usd":
            gbp_converted,converted_symbol = gbp_to_usd(gbp_inp)
        # Add your other cases here. Match cases are much faster in these scenarios.

        case _:
            print("BELLOW? 🙂") # This is basically your ELSE equivalent for match case statements.
            main()

    if not (gbp_converted and converted_symbol):
        print("BELLOW? 🙂") # Basically restart the main loop if we haven't got actual values for the currency symbol and the amount.
        main()

    print(f"£{gbp_inp:.2f} is {converted_symbol}{gbp_converted:.2f}.\n\n") # I taught you formatting strings, and yet you still use regular concatenation. So sad.
    main()
main()