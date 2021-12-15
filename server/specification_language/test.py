from concept import getConcept
from rule import getRuleFormat
import re
from transform import Transform

test1 = "Cho độ dài đoạn thẳng AB = 7cm, biết rằng C là trung điểm của AB. Tính đoạn AC và BC"
test2 = "Cho đoạn thẳng AB có độ dài là 4cm, điểm C nằm giữa hai điểm A và B. M, N lần lượt là trung điểm của AC, BC. Tính đoạn thẳng MN"
test3 = "Cho đoạn thẳng AK có độ dài là 9cm. Cho điểm B thuộc đoạn AK, C nằm giữa hai điểm A và B, biết rằng AC = 4cm, BC = 1cm. Tính đoạn AB và BK"
test4 = "Cho góc XOY = 110, biết rằng Tia OZ là tia phân giác của góc XOY, Tia OP là tia phân giác của góc ZOY, Tia Oz nằm giữa tia OP và Tia OX. Tính các góc ZOY, ZOX, POZ, POX, POY."
test5 = "Cho điểm M thuộc tia OX, Và N thuộc Tia OY, K thuộc tia OX, biết rằng OM + ON = OK, OM = 4cm; ON = 6cm. Tính đoạn MN, OK, MK, NK."
test6 = "Cho đoạn thẳng AB, biết rằng AB = 11cm, M nằm giữa hai điểm A và B, có MB - MA = 5cm. Tính đoạn MA, MB."
test7 = "Cho OI và Tia OK đối nhau. I là giao điểm của Tia IO và đoạn AB, biết rằng góc KOA = 120 (độ), góc BOI = 45 (độ), Tia OA nằm giữa Tia OK và Tia OI, Tia OB nằm giữa Tia OK và Tia OI. Tính các góc KOB, AOI, BOA."
# TODO

test8 = "Cho đường thẳng d, các điểm A, B, C, K đều thuộc d, biết rằng K nằm giữa điểm A và C, C nằm giữa điểm K và B. Điểm O bất kì không thuộc d sao cho góc AOK = 30 (độ), KOC = 40 (độ), AOB = 90 (độ). Tính các góc AOC, COB, KOB"
test9 = "Cho góc XOY = 110, biết rằng Tia OZ là tia phân giác của góc XOY, Tia OP là tia phân giác của góc ZOY, Tia Oz nằm giữa tia OP và Tia OX. Tính các góc ZOY, ZOX, POZ, POX, POY."

engine = Transform()
print("Câu 1:\n" + engine.transformAll(test1) + "\n")
print("Câu 2:\n" + engine.transformAll(test2) + "\n")
print("Câu 3:\n" + engine.transformAll(test3) + "\n")
print("Câu 4:\n" + engine.transformAll(test4) + "\n")
print("Câu 5:\n" + engine.transformAll(test5) + "\n")
print("Câu 6:\n" + engine.transformAll(test6) + "\n")
print("Câu 7:\n" + engine.transformAll(test7) + "\n")
print("Câu 8:\n" + engine.transformAll(test8) + "\n")