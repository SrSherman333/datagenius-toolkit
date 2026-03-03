TRANSLATIONS = {
    "es":{
        "initial_page":{
            "subtitle":"Conjunto de herramientas de cálculo",
            "button":"INICIAR SISTEMA", "btn_lang":"Idioma"},
        "menu_page":{
            "title_menu":"MENÚ", "lbl_information":"Pase el ratón sobre un botón para ver su descripción",
            "btn1":("Temperatura","Calcula la temperatura equivalente en grados Fahrenheit y Kelvin a partir de una temperatura en Celsius"), 
            "btn2":("Almacenamiento","Determina el costo total mensual y anual del almacenamiento en la nube, en función de los GB almacenados y el precio unitario"), 
            "btn3":("Tiempo Ejecución","Calcula el tiempo total (en segundos y minutos) que tarda un programa en ejecutarse, dadas sus operaciones y velocidad de ejecución"),
            "btn4":("Distancia Euclideana","Calcula la distancia euclideana entre dos puntos en un plano cartesiano, utilizando sus coordenadas (x1, y1) y (x2, y2)"), 
            "btn5":("Calificaciones","Calcula la calificación promedio final de un estudiante a partir de cuatro calificaciones individuales"), 
            "btn6":("Interés Simple","Calcula el monto total final a pagar de un préstamo, considerando el capital inicial, la tasa de interés simple y el tiempo en años"),
            "btn7":("Velocidad Promedio","Calcula la velocidad media de un dron en km/h y m/s, dada la distancia recorrida y el tiempo empleado"), 
            "btn8":("Índice Masa Corp.","Calcula el IMC (Índice de Masa Corporal) de una persona, requiriendo su peso en kilogramos y su altura en metros"),
            "btn9":("Consumo Energético","Calcula el consumo energético en kWh de un ordenador durante un mes de 30 días, utilizando su potencia y las horas de uso diario"), 
            "btn10":("Conversión Divisas","Convertir una cantidad de moneda local a su valor equivalente en dólares estadounidenses (USD) y euros (EUR), utilizando los tipos de cambio dados"),
            "btn_back":"Regresar"
            },
        "record":{
            "temperature":{"Celsius":"Celsius","In Fahrenheit":"En Fahrenheit","In Kelvin":"En Kelvin"},
            "storage":{"GB":"GB","Cost per GB":"Costo por GB","Monthly cost":"Costo Mensual",
                    "Annual cost":"Costo Anual"},
            "execution":{"Number of operations":"Número de operaciones",
                        "Execution speed":"Velocidad de ejecución",
                        "Time in seconds":"Tiempo en segundos",
                        "Time in minutes":"Tiempo en minutos"},
            "euclidean":{"Point 1":"Punto 1","Point 2":"Punto 2","Coordinates":"Coordenadas",
                        "Euclidean distance":"Distancia Euclideana"},
            "grades":{"Grades 1 and 2":"Calificaciones 1 y 2","Grades 3 and 4":"Calificaciones 3 y 4",
                    "Grades":"Calificaciones","Average grade":"Promedio"},
            "interest":{"Initial capital":"Capital inicial","Years":"Años",
                        "Annual interest rate(%)":"Tasa de interés anual(%)",
                        "Interest earned":"Interés ganado",
                        "Total amount to be paid":"Monto total a pagar"},
            "drone":{"Distance traveled (km)":"Distancia recorrida (km)",
                    "Time taken (hours)":"Tiempo empleado (horas)",
                    "Average speed in km/h":"Velocidad promedio en km/h",
                    "Average speed in m/s":"Velocidad promedio en m/s"},
            "imc":{"Weight in kilograms(kg)":"Peso en kilogramos(kg)",
                "Height in meters(m)":"Altura en metros(m)", "IMC":"IMC"},
            "energy":{"Hours of the computer operates a day":"Horas del computador operando al día",
                    "Power of the computer(W)":"Energía del computador(W)",
                    "Daily usage | Power consumption":"Uso diario | Consumo de energía",
                    "Monthly consumption":"Consumo mensual"},
            "currency":{"Local currency":"Moneda local","USD rate":"Tasa en USD",
                        "EUR rate":"Tasa en Eur","Dollars | Euros":"Dólares | Euros"}
        },
        "interface1":{
            "title":"CONVERSIÓN DE TEMPERATURA", "frames":("Entrada de Datos","Panel de Resultados"), 
            "label1":"Temperatura en Celsius:", "errors":"Cualquier error aparecerá aquí",
            "buttons_frm1":("CONVERTIR","LIMPIAR"), "label2":"La temperatura en Fahrenheit es:", 
            "label3":"La temperatura en Kelvin es:", "buttons_copy":("COPIAR","COPIAR"),
            "button_back":"Volver al menú"
        },
        "interface2":{
            "title":"COSTO ALMACENAMIENTO EN LA NUBE", "frames":("Entrada de Datos","Panel de Resultados"), 
            "label1":"Cantidad de GB ocupados:", "label2":"Costo por GB:",
            "errors":"Cualquier error aparecerá aquí", "buttons_frm1":("CALCULAR","LIMPIAR"), 
            "label3":"El costo mensual es:", "label4":"El costo anual es:", 
            "buttons_copy":("COPIAR","COPIAR"), "button_back":"Volver al menú"
        },
        "interface3":{
            "title":"TIEMPO DE EJECUCIÓN DE UN PROGRAMA", "frames":("Entrada de Datos","Panel de Resultados"), 
            "label1":"Número de operaciones:", "label2":"Velocidad ejecución (operaciones/segundo):",
            "errors":"Cualquier error aparecerá aquí", "buttons_frm1":("CALCULAR","LIMPIAR"), 
            "label3":"El tiempo en segundos es:", "label4":"El tiempo en minutos es:", 
            "buttons_copy":("COPIAR","COPIAR"), "button_back":"Volver al menú"
        },
        "interface4":{
            "title":"CALCULAR DISTANCIA EUCLIDEANA", "frames":("Entrada de Datos","Panel de Resultados"), 
            "label1":"Valor del punto 1 - x1:", "label2":"Valor del punto 2 - x2:",
            "errors":"Cualquier error aparecerá aquí", "buttons_frm1":("CALCULAR","LIMPIAR"), 
            "label3":"Coordenadas:", "label4":"La distancia Euclideana es:", 
            "buttons_copy":("COPIAR","COPIAR"), "button_back":"Volver al menú"
        },
        "interface5":{
            "title":"PROMEDIO DE CALIFICACIONES", "frames":("Entrada de Datos","Panel de Resultados"), 
            "label1":"Valor de la calificación 1:", "label2":"Valor de la calificación 3:",
            "errors":"Cualquier error aparecerá aquí", "buttons_frm1":("CALCULAR","LIMPIAR"), 
            "label3":"Calificaciones:", "label4":"El promedio es:", 
            "buttons_copy":("COPIAR","COPIAR"), "button_back":"Volver al menú"
        },
        "interface6":{
            "title":"CALCULADORA DE INTERÉS SIMPLE", "frames":("Entrada de Datos","Panel de Resultados"), 
            "label1":"Ingrese el capital inicial:", "label3":"Tasa de interés anual (%):",
            "label2":"Años", "errors":"Cualquier error aparecerá aquí", 
            "buttons_frm1":("CALCULAR","LIMPIAR"), "label4":"El interés ganado es:", 
            "label5":"El monto total a pagar es:", "buttons_copy":("COPIAR","COPIAR"), 
            "button_back":"Volver al menú"
        },
        "interface7":{
            "title":"VELOCIDAD PROMEDIO DE UN DRON", "frames":("Entrada de Datos","Panel de Resultados"), 
            "label1":"Distancia recorrida (km):", "label2":"Tiempo empleado (horas):", 
            "errors":"Cualquier error aparecerá aquí", "buttons_frm1":("CALCULAR","LIMPIAR"), 
            "label3":"Velocidad promedio (km/h):", "label4":"Velocidad promedio (m/s):", 
            "buttons_copy":("COPIAR","COPIAR"), "button_back":"Volver al menú"
        },
        "interface8":{
            "title":"ÍNDICE DE MASA CORPORAL", "frames":("Entrada de Datos","Panel de Resultados"), 
            "label1":"Peso en kilogramos (kg):", "label2":"Altura en metros (m):", 
            "errors":"Cualquier error aparecerá aquí", "buttons_frm1":("CALCULAR","LIMPIAR"), 
            "label3":"IMC:", "label4":"Tabla de IMC: \nPeso inferior: < 18.5 | Peso normal: 18.5 - 24.9 Peso superior: 25.0 - 29.9 | Obesidad: ≥ 30.0:", 
            "buttons_copy":("COPIAR","COPIAR"), "button_back":"Volver al menú"
        }},
    "en":{
        "initial_page":{
            "title":"DATAGENIUS TOOLKIT", "subtitle":"Calculation toolset",
            "button":"START SYSTEM", "btn_lang":"Language"},
        "menu_page":{
            "title_menu":"MENU", "lbl_information":"Hover your mouse over a button to see its description",
            "btn1":("Temperature","Calculate the equivalent temperature in degrees Fahrenheit and Kelvin from a temperature in Celsius"), 
            "btn2":("Cloud Storage Cost","Determine the total monthly and annual cost of cloud storage, based on the GB stored and the unit price"), 
            "btn3":("Execution Time","Calculate the total time (in seconds and minutes) that a program takes to execute, given its operations and execution speed"), 
            "btn4":("Euclidean Distance","Calculate the Euclidean distance between two points on a Cartesian plane, using their coordinates (x1, y1) and (x2, y2)"), 
            "btn5":("Average Grade","Calculate a student's final average grade from four individual grades"), 
            "btn6":("Simple Interest","Calculate the final total amount to be paid on a loan, considering the initial capital, the simple interest rate, and the time in years"),
            "btn7":("Average Speed","Calculate the average speed of a drone in km/h and m/s, given the distance traveled and the time taken"), 
            "btn8":("Body Mass Index","Calculate a person's BMI (Body Mass Index), requiring their weight in kilograms and their height in meters"),
            "btn9":("Energy Consumption","Calculate the energy consumption in kWh of a computer during a 30-day month, using its power and the hours of daily use"), 
            "btn10":("Currency Conversion","Convert an amount of local currency to its equivalent value in US dollars (USD) and euros (EUR), using given exchange rates"),
            "btn_back":"Back"
        },
        "record":{
            "temperature":{"Celsius":"Celsius","In Fahrenheit":"In Fahrenheit","In Kelvin":"In Kelvin"},
            "storage":{"GB":"GB","Cost per GB":"Cost per GB","Monthly cost":"Monthly cost",
                    "Annual cost":"Annual cost"},
            "execution":{"Number of operations":"Number of operations",
                        "Execution speed":"Execution speed", "Time in seconds":"Time in seconds",
                        "Time in minutes":"Time in minutes"},
            "euclidean":{"Point 1":"Point 1","Point 2":"Point 2","Coordinates":"Coordinates",
                        "Euclidean distance":"Euclidean distance"},
            "grades":{"Grades 1 and 2":"Grades 1 and 2","Grades 3 and 4":"Grades 3 and 4",
                    "Grades":"Grades","Average grade":"Average grade"},
            "interest":{"Initial capital":"Initial capital","Years":"Years",
                        "Annual interest rate(%)":"Annual interest rate(%)",
                        "Interest earned":"Interest earned",
                        "Total amount to be paid":"Total amount to be paid"},
            "drone":{"Distance traveled (km)":"Distance traveled (km)",
                    "Time taken (hours)":"Time taken (hours)","Average speed in km/h":"Average speed in km/h",
                    "Average speed in m/s":"Average speed in m/s"},
            "imc":{"Weight in kilograms(kg)":"Weight in kilograms(kg)",
                "Height in meters(m)":"Height in meters(m)", "IMC":"IMC"},
            "energy":{"Hours of the computer operates a day":"Hours of the computer operates a day",
                    "Power of the computer(W)":"Power of the computer(W)",
                    "Daily usage | Power consumption":"Daily usage | Power consumption",
                    "Monthly consumption":"Monthly consumption"},
            "currency":{"Local currency":"Local currency","USD rate":"USD rate",
                        "EUR rate":"EUR rate","Dollars | Euros":"Dollars | Euros"}
        },
        "interface1":{
            "title":"TEMPERATURE CONVERSION", "frames":("Input Section","Results Panel"), 
            "label1":"Enter temperature in Celsius:", "errors":"Any errors will appear here",
            "buttons_frm1":("CONVERT","CLEAN"), "label2":"The temperature in Fahrenheit is:", 
            "label3":"The temperature in Kelvin is:", "buttons_copy":("COPY","COPY"),
            "button_back":"Back to menu"
        },
        "interface2":{
            "title":"CLOUD STORAGE COST", "frames":("Input Section","Results Panel"), 
            "label1":"Enter stored data in GB:", "label2":"Enter cost per GB:",
            "errors":"Any errors will appear here", "buttons_frm1":("CALCULATE","CLEAN"), 
            "label3":"The monthly cost is:", "label4":"The annual cost is:", 
            "buttons_copy":("COPY","COPY"), "button_back":"Back to menu"
        },
        "interface3":{
            "title":"PROGRAM EXECUTION TIME CALCULATOR", "frames":("Input Section","Results Panel"), 
            "label1":"Enter the number of operations:", "label2":"Enter execution speed (operations/second):",
            "errors":"Any errors will appear here", "buttons_frm1":("CALCULATE","CLEAN"), 
            "label3":"The time in seconds is:", "label4":"The time in minutes is:", 
            "buttons_copy":("COPY","COPY"), "button_back":"Back to menu"
        },
        "interface4":{
            "title":"EUCLIDEAN DISTANCE CALCULATOR", "frames":("Input Section","Results Panel"), 
            "label1":"Enter the value of point 1 - x1:", "label2":"Enter the value of point 2 - x2:",
            "errors":"Any errors will appear here", "buttons_frm1":("CALCULATE","CLEAN"), 
            "label3":"Coordinates:", "label4":"The Euclidean distance is:", 
            "buttons_copy":("COPY","COPY"), "button_back":"Back to menu"
        },
        "interface5":{
            "title":"AVERAGE GRADE CALCULATOR", "frames":("Input Section","Results Panel"), 
            "label1":"Enter the value of the grade 1:", "label2":"Enter the value of the grade 2:",
            "errors":"Any errors will appear here", "buttons_frm1":("CALCULATE","CLEAN"), 
            "label3":"Grades:", "label4":"The average grade is:", 
            "buttons_copy":("COPY","COPY"), "button_back":"Back to menu"
        },
        "interface6":{
            "title":"SIMPLE INTEREST CALCULATOR", "frames":("Input Section","Results Panel"), 
            "label1":"Enter the initial capital:", "label2":"Enter the annual interest rate (%):",
            "label3":"Years", "errors":"Any errors will appear here", 
            "buttons_frm1":("CALCULATE","CLEAN"), "label4":"The interest earned is:", 
            "label5":"The total amount to be paid is:", "buttons_copy":("COPY","COPY"), 
            "button_back":"Back to menu"
        },
        "interface7":{
            "title":"AVERAGE SPEED OF A DRONES", "frames":("Input Section","Results Panel"), 
            "label1":"Enter the distance traveled (km):", "label2":"Enter the time taken (hours):", 
            "errors":"Any errors will appear here", "buttons_frm1":("CALCULATE","CLEAN"), 
            "label3":"Average speed in km/h:", "label4":"Average speed in m/s:", 
            "buttons_copy":("COPY","COPY"), "button_back":"Back to menu"
        },
        "interface8":{
            "title":"BODY MASS INDEX CALCULATOR", "frames":("Input Section","Results Panel"), 
            "label1":"Enter the weight in kilograms (kg):", "label2":"Enter the height in meters (m):", 
            "errors":"Any errors will appear here", "buttons_frm1":("CALCULATE","CLEAN"), 
            "label3":"IMC:", "label4":"IMC Table: \nUnderweight: < 18.5 | Normal weight: 18.5 - 24.9 Overweight: 25.0 - 29.9 | Obesity: ≥ 30.0:", 
            "buttons_copy":("COPY","COPY"), "button_back":"Back to menu"
        }
        }
    }