# Ciphers

Cifradores de texto python.

## Cifrados disponibles:
<ul>
	<li><a href="./cifrador-M4X1.py">M4X1</a>. Consiste en trasladar las letras tres lugares hacia atrás.</li>
</ul>

## Modo de uso:
Los archivos tienen dos funciones que son las importante: <codes>cifrar("texto")</codes> y <codes>des_cifrar("qbuql")</codes>, tambien puedes testear las funciones con la funcion <codes>test(show=False)</codes>. O puedes llamar al interprete con solo llamar a la funcion <codes>main()</codes>.
```python
import cifrador-M4X1 as m4x1;
c_text=m4x1.cifrar("hola");#Ciframos.
print("Hola cifrado es: "+c_text);
print(c_text+"desifrado es: "+des_cifrar(c_text));#Desiframos.
m4x1.test();
m4x1.main();#Interprete run.
```
## Dependencia:
Solo el interprete python 3.8 bastara.
