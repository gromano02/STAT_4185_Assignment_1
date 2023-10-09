encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
decrypted_message = list(encrypted_message)
n = len(decrypted_message)
for i in range(1, n//2, 2):
    decrypted_message[i], decrypted_message[n-i-1] = decrypted_message[n-i-1], decrypted_message[i]
x = "".join(decrypted_message)
print(x)
