# Alleles
Simple python script for phenotypic percentage calculation

After importing the Genetica.py, you will be able to use the Parental Class.
Code: from Genetica import Parental

Then, you can define objects in this class. Pass the alleles as one string argument.
Code: mother = Parental("Aa")
      father = Parental("aa")

Methods:

* Procriar(object) : self.result is now an array of the new alleles possibilities

```python
mother.Procriar(father)
print(mother.result)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output: ['Aa', 'Aa', 'aa', 'aa']
                          
* Porcento() : self.porcento is now an array of the alleles appearing percentage

```python
mother.Porcento()
print(mother.porcento)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output: [('Aa', '50.0%'), ('aa', '50.0%')]
                          
* Analise() : shows the percentage

```python
mother.Analise()
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output : Aa : 50.0%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;aa : 50.0%
