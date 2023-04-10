import setuptools

setuptools.setup(
    name='pyvcf2tsv',
    version='0.6.1', 
    description='pyvcf2tsv - conversion of Variant Call Format (VCF) to TSV',
    url='https://github.com/insilicobrain/pyvcf2tsv',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': 'pyvcf2tsv = pyvcf2tsv.main:cli'
    }
)
