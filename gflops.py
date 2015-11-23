from vanity import *

data = array([
        (1961, 8.3e12),
        (1984, 42.78e6),
        (1997, 42.0e3),
        (2000.41, 1300.0),
        (2000.67, 836.0),
        (2003, 100),
        (2007, 52),
        (2011, 1.80),
        (2012, 0.73),
        (2013.5, 0.22),
        (2013.91, 0.16),
        (2013.99, 0.12),
        (2015, 0.08)
        ])


if __name__ == '__main__':
    
    x = data[:,0]
    y = log10(data[:,1])

    fit = polyfit(x, y, 1)
    x_ = arange(1960, 2020, 0.1)
    y_ = polyval(fit, x_)

    ion()
    setup_plotting()

    # Make a figure.
    figure(100, figsize=(10,6))
    hold(True)
    semilogy(x, 10**y, 'o', markerfacecolor=pomegranate,\
            markeredgecolor=pomegranate, markersize=10, alpha=0.75) 
    semilogy(x_, 10**y_, linewidth=4, color=belize_hole, alpha=0.8)
    grid(True)
    ylabel('US Dollars (Inflation Adjusted to 2013)')
    xlabel('Time (Years)')
