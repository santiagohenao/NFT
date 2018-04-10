rm -f *.dat *.png NFT
rm -r -f results
F0=0
FF=1
STEP=0.0001
FILENAME="./data/OGLE-SMC-T2CEP-02.dat"
#FILENAME="./datos.dat"
python3 datos.py > datos.dat
python3 graficar.py $FILENAME


time -f "Tiempo compilando (C++): \t\t%e"  c++ NFT.cpp -o NFT
time -f "Tiempo calculando (C++): \t\t%e" ./NFT $FILENAME $F0 $FF $STEP "transf_c.dat"
time -f "Tiempo graficando (Python, C++): \t%e" python3 graficar.py "transf_c.dat"
time -f "Tiempo calculando (Julia): \t\t%e" julia NFT.jl $FILENAME $F0 $FF $STEP  "transf_julia.dat"
time -f "Tiempo graficando (Python, Julia): \t%e" python3 graficar.py "transf_julia.dat"
#time -f "Tiempo calculando (Python): \t\t%e" python3 NFT.py $FILENAME $F0 $FF $STEP  "transf_python.dat"
#time -f "Tiempo graficando (Python, Python): \t%e" python3 graficar.py "transf_python.dat"


#rm -f *.dat NFT
mkdir results
mv *.png results/
mv *.dat results

python3 period.py "./results/transf_c.dat"
