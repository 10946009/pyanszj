import sys

sky = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
gnd = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

for n in sys.stdin:
    n = int(n)

    n = (n -1744) % 60
    print("%s%s" % (sky[n % 10], gnd[n % 12]))
