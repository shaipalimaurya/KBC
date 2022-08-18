question_list=[
    ["which is the capital of India?"],
    ["who is the prime minister of India?"],
    ["which course teach in Navgurukul?"],
    ["who is the father of India?"]
]
option=[
    ["Goa","Karnataka","Kerala","New Delhi"],
    ["Rajnath Kovind","Javaharlal Nehru","Narendra Modi","Atul Bihari Vajpei"],
    ["Software Engineering","Agriculture","Science and Technologyg","Medical coures"],
    ["Mahatma Gandhi","Rajnath Kovind","Atul Bihari Vajpei","APJ Abdul Kalam"],
]
option50_50=[
    ["1)Goa","4)New Delhi"],
    ["2)Jawaharlal Nehru","3)Narendra Modi"],
    ["1)Software Engineering","3)Science and Techonology"],
    ["1)Mahatma Gandhi","2)APJ Abdul Kalam"],
    ["1)Mahatma Gandhi","2)APJ Abdul Kalam"],
]
ans_list=[4,3,1,1]
print("kon banega karodpati,kbc")
print("lets start the game")
i=0
c=0
s=10000
while i<len(question_list):
    print(question_list[i])
    a=0
    while a<len(option[i]):
        k=option[i][a]
        print(a+1,k)
        a=a+1
    if c==0:
        life_line=input("do you want to use lifeline n/y:-")
        if life_line=="yes":
            c=c+1
            print(option50_50[i])
    answer=int(input("enter the option"))
    if ans_list[i]==answer:
        print("your answer is correct",s)
        s=s+10000
    else:
        print("your answer is wrong")
        break
    i=i+1