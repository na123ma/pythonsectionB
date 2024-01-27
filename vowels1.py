def index(str):
      vowels='aeiouAEIOU'
      out=''
      for i in vowels:
            if i not in str:
                  out+=i
      return out
print(index('hello'))  