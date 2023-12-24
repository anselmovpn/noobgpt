print("este programa é uma calculadora de média entre 3 notas de 0 a 10")
n1 = float(input("digite a primeira nota "))
n2 = float(input("digite a segunda nota "))
n3 = float(input("digite a terceira nota "))

if 0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10:
    media = (n1+n2+n3)/3
    media_f = round(media,2)
    print(f"a média entre essas 3 notas fornecidas é {media_f}")
else:
    print ("você digitou algum(ns1) valor que não esteja entre 0 e 10")
