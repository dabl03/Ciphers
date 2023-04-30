# Ciphers

Cifradores de texto python.

## Cifrados disponibles:
<ul>
	<li><a href="./cifrador_M4X1.py">M4X1</a>. Consiste en trasladar las letras tres lugares hacia atrás.</li>
</ul>

## Modo de uso:
Los archivos tienen dos funciones que son las importante: `m4x1.cifrar("texto")` y `m4x1.des_cifrar("qbuql")`, también puedes testear las funciones con la función `test(show=False)`. O puedes llamar al interprete con solo llamar a la función `main()`.
```python
from cifrador_M4X1 import *;
c_text=m4x1.cifrar("hola");#Ciframos.
print("Hola cifrado es: "+c_text);
print(c_text+" descifrado es: "+m4x1.des_cifrar(c_text));#Desciframos.
test();
main();#Interprete run.
```
O también puedes llamar al interprete o al tester desde la consola:
```bash
echo Testeamos la función con --t o tester.
python -m ./cifrador_M4X1.py --tester
echo Ejecutamos normalmente:
python -m ./cifrador_M4X1.py
echo Para más información de las opciones disponibles ingrese --h o --help
```
## Dependencia:
Solo el interprete python 3.8 bastara.
