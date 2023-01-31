/*
 * Série de exercícios 1 (parte integrante do Laboratório 1)
 *
 * Dentro do tema do programa de conversão de temperaturas (consultar
 * enunciado do laboratório), faça um programa que exibe as 
 * temperatura em Fahrenheit de 0 até 200 F, com incrementos de 20 F. 
 * À frente de cada valor em Fahrenheit deve exibir o valor 
 * correspondente em Celsius.
 */

using System;

namespace LabsCSharp
{
    class FahrCelsius2
    {
        static void Main()
        {
            for (double fahr = 0; fahr <= 200; fahr += 20)
                Console.WriteLine("F: {0,6:F}  C: {1,6:F}", fahr, (5.0/9)*(fahr - 32));

            Console.ReadKey(true);
        }
    }
}