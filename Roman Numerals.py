class Solution:
    def romanToInt(self, s: str) -> int:
        RomanNumeralDict = {
            "I"    :     1,
            "V"    :     5,
            "X"    :     10,
            "L"    :     50,
            "C"    :     100,
            "D"    :     500,
            "M"    :     1000
        }
        Conversion = 0
        SplitString = []

        if "IV" in s or "IX" in s:
            s = s.replace("IV","IIII")
            s = s.replace("IX","VIIII")

        if "XL" in s or "XC" in s:
            s = s.replace("XL","XXXX")
            s = s.replace("XC","LXXXX")

        if "CD" in s or "CM" in s:
            s = s.replace("CD","CCCC")
            s = s.replace("CM","DCCCC")

        for char in s:
            SplitString.append(char)

        for numeral in SplitString:
            if numeral in RomanNumeralDict:
                Conversion += RomanNumeralDict[numeral]

        return Conversion
string = "CDXLVII"
a = Solution()
x = a.romanToInt(string)
print(x)