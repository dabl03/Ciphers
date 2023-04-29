# Ciphers



Cifradores de texto python.

## Cifrados disponibles:
<ul>
	<li><a href="./cifrador_M4X1.py">M4X1</a>. Consiste en trasladar las letras tres lugares hacia atrás.</li>
</ul>

## Modo de uso:
Los archivos tienen dos funciones que son las importante: `cifrar("texto")` y `des_cifrar("qbuql")`, tambien puedes testear las funciones con la funcion `test(show=False)`. O puedes llamar al interprete con solo llamar a la funcion `main()`.
```python
import cifrador_M4X1 as m4x1;
c_text=m4x1.cifrar("hola");#Ciframos.
print("Hola cifrado es: "+c_text);
print(c_text+" desifrado es: "+m4x1.des_cifrar(c_text));#Desiframos.
m4x1.test();
m4x1.main();#Interprete run.
```
## Dependencia:
Solo el interprete python 3.8 bastara.
