from zipenumerate_challenge import annual_births_average

def test_output():
    year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    births = [723_165, 723_913, 729_674, 698_512, 695_233, 697_852, 696_271, 679_106, 657_076, 640_370]
    run_avg = [723165, 723539, 725584, 718816, 714099, 711392, 709231, 705466, 700089, 694117]
    expected = list(zip(year, births, run_avg))
    actual = annual_births_average(year, births)
    assert expected == actual