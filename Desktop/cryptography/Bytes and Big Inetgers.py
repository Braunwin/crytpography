from Crypto.Util.number import long_to_bytes

# The integer you want to convert back (this number was derived from a message)
message_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269 # Example integer derived from 'Hello'

# --- Step 1: Convert the Integer back to Bytes ---
# long_to_bytes() takes the integer and returns the corresponding byte string.
reverted_bytes = long_to_bytes(message_integer)

# --- Step 2: Decode the Bytes to a Human-Readable String (Message) ---
# You must use the encoding that was originally used (e.g., 'utf-8').
try:
    decoded_message = reverted_bytes.decode('utf-8')
    
    print(f"Input Integer:   {message_integer}")
    print(f"Reverted Bytes:  {reverted_bytes}")
    print(f"Decoded Message: {decoded_message}")

except UnicodeDecodeError:
    print("Error: Could not decode bytes into a message (check the encoding).")

