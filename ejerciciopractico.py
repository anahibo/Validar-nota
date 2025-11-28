nota = float(input("Ingrese una nota entre 0 a 20:")) 
if nota <0 or nota >20:
    print ("Nota fuera del rango")
elif nota>= 18 and nota <=20:
    print ("Sobresaliente")
    if nota >=19.5:
        print ("Candidato a mencion de honor")
elif nota >=16 and nota<= 17.99:
    print ("Muy Bueno")
elif nota >= 14 and nota <= 15.99:
    print ("Bueno")
elif nota >=12 and nota <=13.99:
    print ("Suficiente")
elif nota >=0 and nota <= 11.99:
    print ("Insuficiente")
    if nota <8:
        print ("Debe asisitir a tutorias obligatorias")