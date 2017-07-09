import random

M = 1000
secret = random.randint(1,M)
guess = 0
tries = 0
times = 12

print ("啊！我是猜数机器人。我有一个秘密数字。")
print ("这个数在1到%s之间，我给你%s次机会。 " % (M, times))

while guess !=secret and tries < times:
    guess = input("你还有%s次机会，你猜哪个数？ " % (times-tries))
    guess = int(guess)
    if guess < secret:
        print("太小了！")
    elif guess > secret:
        print("太大了！")
    tries = tries+1
if guess == secret:
    print ("耶！找到我的秘密数字了！")
else:
    print ("没有机会了。祝你下次好运！")
    print ("秘密数字是",secret)
    
