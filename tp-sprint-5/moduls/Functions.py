class Funciones:
    def calcular_monto_total(Monto_Dolares):

        Impuesto_Pais = Monto_Dolares * 0.25 #calcula el impuesto pais(25%) del Monto_Dolares
        Impuesto_Ganancias = Monto_Dolares * 0.35  #calcula el impuesto ganancias (35%) del Monto_Dolares
        Total = Monto_Dolares + Impuesto_Pais + Impuesto_Ganancias # el total es el Monto_Dolares mas los impuestos calculados
        
        return  Total  

    def descontar_comision(monto,comision_porcentaje):

        comision = comision_porcentaje / 100 #toma el valor del porsentaje (ej -90-) y lo convierte en decimal (ej -0,9-)
        descuento = monto * comision #mutiplico monto por el pocentaje del monto para sacar la comision que tngo que cobrar
        descontar_comision = monto - descuento #resto a monto la comision que calcule 
        
        return descontar_comision 

    def calcular_monto_plazo_fijo(monoto_plazo_fijo): 
        
        tasa = 133 #tasa de interes del plazo fijo
        dias = 60  #dias que se realizara (se podria ingresar hasta 365)
        intereses = monoto_plazo_fijo * ((tasa/100) * dias / 365) #calculamos el interes que generara el plazo fijo, sacanco el % del monto y el % en dias restando en el monto
        
        return intereses #solo devuele el generado para tener un total debemos sumarle al monto intereses 