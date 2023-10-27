

class StringRev:
    def reverse_string(self, text):
        self.text = list(text)
        return "".join(self.text[::-1])
        


txt = StringRev()
text = input("Enter a String : ")
print(f"Reverse of '{text}' is '{txt.reverse_string(text)}'")
