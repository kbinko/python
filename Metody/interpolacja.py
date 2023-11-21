import numpy as np
import pylab


def interplin2p(x, xi, yi, xil, yil):
    return yil + (x - xil) * (yi - yil) / (xi - xil)


def interplinvect(x, xyvect):
    xinterp = []
    yinterp = []
    
    for xk in x:
        N = len(xyvect[0])
        for i in range(0, N-1):
            if (xk >= xyvect[0][i] and xk < xyvect[0][i+1]):
                xinterp.append(xk)
                yinterp.append(interplin2p(xk, xyvect[0][i], xyvect[1][i], xyvect[0][i+1], xyvect[1][i+1]))
            i += 1
    return [xinterp, yinterp]


xyv_cos = []
xyv_cos.append([i for i in np.arange(0.1, 3.3, 0.1)])
xyv_cos.append([np.cos(1/i) for i in xyv_cos[0]])


xyv_exp = []
xyv_exp.append([i for i in np.arange(0, 3.3, 0.1)])
xyv_exp.append([np.exp(np.sin(i)) for i in xyv_exp[0]])


xin = [i for i in np.arange(0, 3.3, 0.08)]


xyinterp_cos = interplinvect(xin, xyv_cos)
xyinterp_exp = interplinvect(xin, xyv_exp)


pylab.figure(figsize=(16, 8))


pylab.subplot(1, 2, 1)
pylab.plot(xyv_cos[0], xyv_cos[1], 'o', label='Oryginalne dane')
pylab.plot(xyinterp_cos[0], xyinterp_cos[1], '.-', label='Interpolowane Dane')
pylab.title('Interpolacja cos(1/x)')
pylab.legend()

pylab.subplot(1, 2, 2)
pylab.plot(xyv_exp[0], xyv_exp[1], 'o', label='Oryginalne Dane')
pylab.plot(xyinterp_exp[0], xyinterp_exp[1], '.-', label='Interpolowane dane')
pylab.title('Interpolacja exp(sin(x))')
pylab.legend()

pylab.tight_layout()
pylab.show()
