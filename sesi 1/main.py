import random     # mengambil library 



welcome_masage = "selamat datang cuy"
posision_cuy= random .randint (1,4) #mengambil angka rendom dengan format integer

print ("******************************")
print ("**{welcome_masage}**")
print ("******************************")

name_user = input ("masukan nama anda :")
print (f'''
hello {name_user} coba perhatikan goa di dalam ini 
|_| |_| |_| |_|
''')
pilihan_user = int(input ("menurut kamu nomer berapa yang terdapat goa di atas ?[1/2/3/4]:"))
print (f"pilihan kamu adalah {pilihan_user}")

if pilihan_user ==posision_cuy:
    print (f"selamat {name_user} kamu menang posisi goa ada di {posision_cuy} dan pilihanmu adalah {pilihan_user}.")
else :
    print(f"kamu salah goa bukan berada disitu tapi ada di goa nomer {posision_cuy} sedangkan kamu memilih goa {pilihan_user}")    