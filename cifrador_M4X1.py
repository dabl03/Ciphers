import base;
"""
     Programa que cifra usando el cifrado M4X1
    class m4x1:
        Funciones disponibles:
        cifrar : Cifra usando el formato m4x1. Si no entiendes como es: Consiste en trasladar las letras tres lugares hacia atrás. (M4X1)[https://gravityfalls.fandom.com/es/wiki/Lista_de_Criptogramas#:~:text=Tabla%20de%20Cifrado-,Tabla%20de%20Cifrado%20%22M4X1%22,Consiste%20en%20trasladar%20las%20letras%20tres%20lugares%20hacia%20atr%C3%A1s.,-Criptograma]
        des_cifrar : descifra.
        test: Hace un test de esta clase.
"""
class m4x1:
    c_abc="xyzabcdefghijklmnopqrstuvw";#El alfabeto cifrado.
    name="M4X1";#Nombre del cifrado.
    width=60;#Longitud del titulo que se enseñara en el interprete.
    def cifrar(str_) -> str:
        """
            Cifra un texto.
            Retorna None si se pasa un argumento invalido.
        """
        if not base.is_str_and_not_void(str_): return None;
        cifrado="";
        for char in str_:
            n_char=ord(char);
            #Comprobación
            if not char.isalpha():
                cifrado+=char;
                #char>"b":
            elif ord(char.lower())>ord('c'):
                #Retrocedemos 3 caracteres.
                cifrado+='%c'%(n_char-3);
            else:
                #a: x, b: y, c: z
                if n_char>90:
                    na=ord('a');
                    nz=ord('z');
                else:
                    na=ord('A');
                    nz=ord('Z');
                #   z-(if a:2, b:1, c:0)
                out="%c"%(nz-(2-(n_char-na)))
                cifrado+=out;
        return cifrado;
    def des_cifrar(cifrado="")->str:
        """
            Descifra un texto.
            Retorna None si se pasa un argumento invalido.
        """
        if not base.is_str_and_not_void(cifrado): return None;
        d_cifrado="";
        for char in cifrado:
            if not char.isalpha():
                d_cifrado+=char;
            elif ord(char.lower())<ord('x'):
                d_cifrado+='%c'%(ord(char)+3);
            else:
                au=ord(char.lower())-ord('x');
                d_cifrado+='%c'%((ord('a') if char.islower() else ord('A'))+au);
        return d_cifrado;

def test(show=True)->int:
    """Testea la clase m4x1 usando el tester del archivo base."""
    status=base.test(
        m4x1.c_abc,
        "cifrar",
        m4x1.cifrar,
        base.normal,
        show
    );
    if status==-1:
        return -1;
    return base.test(
        base.abc,
        "des_cifrar",
        m4x1.des_cifrar,
        [m4x1.cifrar(str_) for str_ in base.normal],
        show,
        m4x1.c_abc
    );
def main():
    """Llama al interprete base pasándole el cifrador m4x1"""
    return base.main(m4x1);

if __name__ == '__main__':
    from sys import argv;
    if len(argv)>1:
        mode=base.tratar_arg(argv);
    if "tester" in mode:
        test(True);
    else:
        main();
