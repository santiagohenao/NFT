#=
Non-equidistant Fourier Transform
Uso: julia NFT.jl "input.dat" f0 ff step "output.dat"
=#

I=im
len=length
str=string

#=
function SingleFT(t::Float64, y::Float64, f::Float64)
    """
    Single iteration of fourier transform
    """
    return y*exp(-2.0*pi*I*f*t)
end
=#

SFT=(t,y,f)->y*exp(-2.0*pi*I*f*t)

filename=ARGS[1]
f0=float(ARGS[2])
ff=float(ARGS[3])
step=float(ARGS[4])
outname=ARGS[5]

file=readlines(open(filename))
X=zeros(length(file))
Y=zeros(length(file))
for i in 1:length(file)
    X[i]+=float( split(file[i])[1] )
    Y[i]+=float( split(file[i])[2] )
end
Y=Y-mean(Y)

#=
transf=[]

for freq in f0:step:ff
    FT=(t,y)->SFT(t,y,freq)
    push!(transf,sum(map(FT,X,Y)))
end
=#


open(outname, "w") do outf
    for freq in f0:step:ff
        FT=(t,y)->SFT(t,y,freq)
        s = abs(sum(map(FT,X,Y)))
        write(outf, str(freq)*"\t"*str(s)*"\n" )
    end
end
