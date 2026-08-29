# Elección de las 5 series de datos

## 1. Base monetaria

- id_variable = 15,
- descripcion = Base Monetaria
- periodicidad = D
- unidad = En millones de ARS
- primerFechaInformada = 1996-01-02

*Razon de Elección:* Me parece una variable importante y tomarla como la primera para poder observar la evolucion de la totalidad del dinero legal del pais.

*Elegido por sobre:* Circulacion monetaria, esto porque la base monetaria me parece un variable mas general que esta.

## 2. Inflacion Mensual

- id_variable = 27
- descripcion = Inflacion mensual
- periodicidad = M
- unidad = En porcentaje
- primerFechaInformada = 1943-03-31

*Razon de Elección:* Otra variable tan importante como la base monetaria, y también porque en este pais es el tema que más se habla por escandalo en el rubro economico.

*Elegido por sobre:* Inflacion Interanual, porque esta variable es tranquilamente calculable usando la inflacion mensual.

## 3. Reservas Internacionales

- id_variable = 1
- descripcion = Reservas internacionales
- periodicidad = D
- unidad = En millones de USD
- primerFechaInformada = 1996-01-03

*Razon de Elección:* Es interesante mantenerse informado de las subidas y bajadas de las reservas internacionales del pais.

## 4. Tipo cambiario minorista

- id_variable = 4
- descripcion: = Tipo de cambio minorista (promedio vendedor)
- periodicidad = D
- unidad = Pesos argentino por dolar
- primerFechaInformada = 2010-06-01

*Razon de Elección:* Se eligió esta variable porque el argentino promedio siempre esta pendiente del valor del dolar de forma practicamente diaria.

*Elegido por sobre:* Tipo de cambio mayorista de referencia, el cambio minorista se tendria más en cuenta que el mayorista.

## 5. Tasa de Interes BADLAR de bancos privados (TNA)

- id_variable = 7
- descripcion = Tasa de interes BADLAR de bancos privados
- periodicidad = D
- unidad = En porcentaje nominal
- primerFechaInformada = 1999-01-04

*Razon de Elección:* Estar al tanto de como cotizan los interes en los bancos privados para saber cuando y donde invertir un monto minimo de 1 millon de pesos.

*Elegido por sobre:* Tasa de interes TM20 de bancos privados, esta tasa sirve para aquellos que quieran invertir en montos iguales o mayores a los 20 millones de pesos, por lo tanto no es tan accesible invertir de esa forma. Prefiero BADLAR por eso mismo. 

Y respecto a la misma tasa de interes pero en porcentaje efectivo, la tasa elegida tiene información desde 1999 mientras que la tasa de interes en porcentaje efectivo tiene historial desde 2020. Un detalle más sobre esto, estas tasas expresan lo mismo pero diferente forma, la que se eligió es una tasa nominal (TNA), mientras la otra es tasa efectiva, esto para dejar claro que cuando esten los marts de esta variable, sean visto como lo que son, porcentajes nominales.

## Detalles:

### Granularidad mixta

Son todas variables con periodicidad diaria menos la Inflacion Mensual, que es de periodicidad mensual, se decidio mantener esta variable por gran interes que tiene en el mercado, además de que se asumira la ausencia que puede generarse en las extracciones de los datos.

### Ninguna Serie se actualiza el mismo día

Cada una tiene su propio rezago de publicación. Esto refuerza lo de la granularidad mixta: "hoy esta serie no trajo nada" es el estado normal, no una excepción — le pasa a las diarias también, no solo a la mensual. Nuevamente esto en el proceso de extracción se tendrá presente.
