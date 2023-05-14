import os
import re
import subprocess
import pdb


def download():
    
    # File URLs.
    urls = {
    "HLCA":['"https://corpora-data-prod.s3.amazonaws.com/4e08dac3-2ecb-4906-a7a9-21c980c97e61/local.h5ad?AWSAccessKeyId=ASIATLYQ5N5X3RYPFKVA&Signature=tSmZB9l%2BNMj%2BG9sSjRpDS8wdmvk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIGIqywOhmzVUZv1SrMSOJaYaCS1v86ldMYEkE%2FY0QptJAiATNrmFD2bIr1brOIFB3yX1OwQqNPlfNjEOxAcNkx7fBSr0AwiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDIzMTQyNjg0NjU3NSIM6p1IaVqBKTXR8G%2BRKsgD2z%2FXS4LzUzTysEll2kzwaESysCn%2BhCXFkF53BRL1ZFet52%2BHHSmVZO90GGyPQ7I49Q84k7XmEdOcRYBLkmIvjORsIVcOiy55%2BeFQTbShEeiqatEB67Aieatm5SKQzEkCMuq119x7IQM%2FuHnMoGWo5rzMBcQT%2FJtOY1dC09oO3p%2FIYWmBncAW0E1bMom3qu6WUmEdZhxjlSZ8KC%2BEEM28%2BRp1B%2F%2BDApi1TbdetBkUUC7isln%2FkDSCLyOdSiSCks%2BPvu5neRGYoH2rDf2varIz0krHfB7AGyHIj2JWseSj2JQVOGpTMdGuFtRaKW0POvtUIm5pTnKJ4CP0RcawtvKHQ6ayIpYAS8LuthdJljRiTchGlSAJHMsTZXupu7R%2FUEoOCRHds4ns132O9yeB6r%2FzDBDPWNQFhdM8YxxNf%2B0Bn4ymE42ridtjtq1zh30flfvjcNxWJVadcuNVNXkx2P9Qgy7oxSqUcqKFrghkmzE95JZrvEmWP%2FBh17hI6hxmxSmB%2FiI96sBw3Y9o9fGyzGwzsA4%2Fx3yLCGdfAL9FP%2BoCNIoYX5C5rEm2GpNSpz2tSwGUuJM1zqvWCg8mx%2BK6QhPwz55CncUzWNZCMK%2FV7qIGOqYBbLS8nxHxcxu9zjW7%2BKYSApi%2BRTr5Ey3VdTBbBSdzdfetqN3tlKO2UEts6CCNxoxqCPsx1zQh%2BhohyME2v7W8EDH8MGr2n%2BzihGnD3%2BaJQGHOu%2BlukqyI2%2FdiI%2FKr%2FT%2F11MJv5UxkzxVRwM7VkHPQYN4dzKney5E3mk0VmvKdJyjfLOqyplE8GLAdCEBrU2LR5G97k2SpEVDvB8I7NOfPpIeEEXxoLg%3D%3D&Expires=1684349159"'],
        
    "Yale IPF":[''],
    "Cararro":['https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4272nnn/GSM4272918/suppl/GSM4272918_dd10_filtered_feature_bc_matrix.h5',    
               'https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4272nnn/GSM4272919/suppl/GSM4272919_dd39_filtered_feature_bc_matrix.h5',
               'https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4272nnn/GSM4272915/suppl/GSM4272915_cc04_filtered_feature_bc_matrix.h5',
               'https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4272nnn/GSM4272916/suppl/GSM4272916_cc05_filtered_feature_bc_matrix.h5',
               'https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4272nnn/GSM4272917/suppl/GSM4272917_dd09_filtered_gene_bc_matrices_h5.h5',
               'https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4272nnn/GSM4272920/suppl/GSM4272920_dd49_filtered_feature_bc_matrix.h5'
              ],
    "Nuclear-seq":['']
    }

    # Create data folders
    if not os.path.exists("data"):
        os.mkdir("data")
    if not os.path.exists(f"data/GSE143706"):
        os.mkdir(f"data/GSE143706")
    if not os.path.exists("results"):
        os.mkdir("results")

    # Download all data
    print("===========================")
    for dname in urls.keys():

        print(f"Downloading data for: {dname}...")

        for url in urls[dname]:
            if url != '':
                if dname == "Cararro":
                    cmd = f"cd data/GSE143706 && wget -q {url}"
                else:
                    cmd = f"cd data && curl -o local.h5ad {url}"
                res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{dname} finished")
        
    print("If download of HLCA dataset was not successful. You may head to https://cellxgene.cziscience.com/collections/6f6d381a-7701-4781-935c-db10d30de293 and download the core HLCA dataset and rename it as 'local.h5ad' and save it under data/")
    return None

if __name__ == "__main__":
    download()