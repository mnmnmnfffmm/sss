a, b= map(int, input().split())

print('1000원:',(b-a)//1000)
print('500원:',(b-a)%1000//500)
print('100원:',(b-a)%1000%500//100)
print('50원:',(b-a)%1000%500%100//50)
print('10원:',(b-a)%1000%500%100%50//10)