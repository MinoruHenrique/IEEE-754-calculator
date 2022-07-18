import math

class CalculadoraBinaria:

    def __init__(self,long_mantisa,long_exp):#Método constructor
        #Variables de instancia

        #Longitud de mantisa
        self.longitud_de_mantisa=long_mantisa

        #Longitud del exponente
        self.longitud_de_exponente=long_exp

        #Sesgo
        self.sesgo=None
        self.calcular_sesgo()

    @staticmethod
    def convertir_a_binario(num):#Metodo para convertir números en base decimal a binaria

        ###Funciones útiles para calcular el número en binario###
        ###---------------------------------------------------###
        def convertir_parte_entera(ent):#Convierte la parte entera a binaria
            if (ent == 0):
                return "0"
            ent_bin = ""
            while (ent > 0):
                cociente = ent // 2
                residuo = ent % 2
                ent_bin = str(int(residuo)) + ent_bin
                ent = cociente
            return ent_bin

        def convertir_parte_decimal(dec):#Convierte la parte decimal a binaria
            dec_bin = ""
            for i in range(50):
                dec, nueva_cifra = math.modf(dec * 2)
                dec_bin += str(int(nueva_cifra))
            return dec_bin
        ###---------------------------------------------------###

        if (num == int(num)):#Si el numero es entero, no es necesario calcular el decimal en binario
            return convertir_parte_entera(num),"0"*80

        #Se separa el número en base decimal en su parte entera y decimal con math.modf
        decimal,entero=math.modf(num)

        #Transformar parte entera y binaria
        entero_bin=convertir_parte_entera(entero)
        decimal_bin=convertir_parte_decimal(decimal)

        #Retorna el número entero en binario

        return entero_bin,decimal_bin

    def calcular_sesgo(self):
        self.sesgo=(2**(self.longitud_de_exponente-1))-1

    def convertir_formato_IEEE(self,num):
        if num==0:#Si el número es cero, todos los bits tienen valor cero
            signo="0"
            exponente=""
            mantisa=""

            for i in range(self.longitud_de_exponente): exponente+="0"
            for i in range(self.longitud_de_mantisa): mantisa += "0"

            palabra_IEEE=signo+" "+exponente+" "+mantisa

            return palabra_IEEE
        elif num>0:#Asignación del signo correspondiente
            signo="0"
        elif num<0:
            signo="1"


        entero,decimal=CalculadoraBinaria.convertir_a_binario(abs(num)) #Convertir a binario el número

        exponente=len(entero)-1+self.sesgo

        def aproximar(numero,long):#Metodo para aproximar el numero
            if(numero[long]=="0"):
                return numero[:long],""
            else:
                num_b10=CalculadoraBinaria.binario_a_decimal(numero[:long])
                num_b10=int(num_b10)+1
                return CalculadoraBinaria.convertir_a_binario(num_b10)

        mantisa=entero[1:]+decimal  #Ya que el primer bit siempre es 1, no contamos con este
        mantisa,t= aproximar(mantisa,long=self.longitud_de_mantisa) #Aproxima la mantisa para acomodarlo#
                                                                  #a la cantidad de bit de la mantisa #

        exponente,t=CalculadoraBinaria.convertir_a_binario(exponente)
        
        def acomodar_longitud(num,long):
            while(len(num)!=long):
                num="0"+num
            return num
        exponente=acomodar_longitud(exponente, self.longitud_de_exponente)
        palabra_IEEE=signo+" "+exponente+" "+mantisa    #Concatena las tres partes de manera separada

        return palabra_IEEE
    def calcular_epsilon(self):
        base=2
        epsilon = (base ** (-self.longitud_de_mantisa+1))/2
        return epsilon
    def calcular_maximo(self):
        base = 2
        maximo = (1-base**(-self.longitud_de_mantisa))*base ** (base ** self.longitud_de_exponente-self.sesgo)
        return maximo
    def calcular_min(self):
        base=2
        minimo = base ** (- self.sesgo)
        return minimo

    def validacion(palabra): #Para corroborar de que el numero binario ingresado es valido
        conjunto=set(list(palabra))
        if (('0'in conjunto or '1'in conjunto) and len(conjunto) in {1,2}):
            return 0
        else:
            return 1

    def binario_a_decimal(num): #Convertimos el numero binario en decimal

        def parte_entera(entero): #La parte entera del numero binario

            bits=list(entero)
            valor=0
            for i in range(len(bits)):
                bit=bits.pop()
                if(bit=='1'):
                    valor =valor +pow(2,i)
                
            return float(valor)    
                    
        def parte_decimal(decimal): #La parte decimal del numero binario

            bitss=list(decimal)
            valore=0
            for i in range(len(bitss)):
                if(bitss[i]=='1'):
                    valore=valore + pow(0.5,i+1)
                    
            return float(valore)

        numero=num.split(",") #Se separa la parte entera y decimal

        if(len(numero)==1):
            return parte_entera(numero[0]) #Si no tiene parte decimal se retorna la parte entera en base 10

        #Si tiene parte decimal
        p_entera=parte_entera(numero[0])
        p_decimal=parte_decimal(numero[1])

        return p_entera +p_decimal 

    
    def palabra_a_decimal(self,palabraieee): #Metodo para convertir la palabra a un numero decimal
        palabraieee=palabraieee.replace(" ","")
        if (CalculadoraBinaria.validacion(palabraieee)==0 and len(palabraieee)==(1+self.longitud_de_exponente+self.longitud_de_mantisa)):
            lista=list(palabraieee)
            signo=1
            exponente=""
            numero=""

            if(lista[0]=='1'):
                signo=signo-2

            for i in range(self.longitud_de_exponente):
                exponente=exponente+lista[i+1]

            exp_decimal=CalculadoraBinaria.binario_a_decimal(exponente)

            num_exp=int(exp_decimal)-self.sesgo

            if(num_exp>=0):
                for i in range(self.longitud_de_mantisa):
                    if(i==num_exp):
                        numero=numero+','
                    numero=numero + lista[i+1+self.longitud_de_exponente]
                numero='1'+numero
    

        return signo*CalculadoraBinaria.binario_a_decimal(numero)

if __name__ == "__main__":

    print("_____FORMATO IEEE_____")
    datos=CalculadoraBinaria(int(input("Ingrese longitud de la mantisa: ")),int(input("Ingrese longitud del exponente: ")))
    
    
    print("""
         Sesgo del ordenador: {}
         Epsilon:             {}
         Valor mínimo:        {}
         Valor máximo:        {}
         """.format(datos.sesgo,datos.calcular_epsilon(),datos.calcular_min(),datos.calcular_maximo()))
   
    numero1=float(input("Ingrese el numero que quiere convertir al formato IEEE: "))
    print("Formato ieee: "+ datos.convertir_formato_IEEE(numero1))

    numero2=str(input("Ingrese el numero formato ieee que quiere llevarlo a decimal: "))
    print("Numero decimal: ",datos.palabra_a_decimal(numero2))
