while True:
  try:
    n = int(input())      # 取得接下來有幾個數
    arr = []              # 建立排序用的串列

    for i in range(n):
      p, q = map(int, input().split())
      arr.append([p, q])  # 陸續將題目提供的兩個數字，轉換成串列存入 arr

    output = sorted(arr)  # output 為 arr 由小到大排序
    for i in output:
      print(*i)           # 輸出 output 內容
  except:
    break
