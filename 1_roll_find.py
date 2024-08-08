



import pandas as pd

df=pd.read_csv("output.csv")
arr_data=[]
n=0
for api in df["filename"]:
    #print(api)
    br_find=api.find("_")
    do_find=api.find(".")
    paper_code=str(api[br_find+1:do_find])

    roll=str(api[:br_find])
    scgpa=str(df["sgpa"][n])
    cgpa=str(df["cgpa"][n])
    if scgpa=="nan" and cgpa=="nan":
        pass
    else:
        
        new_js={
            "roll":roll,
            "paper_code":paper_code,
            "scgpa":scgpa,
            "cgpa":cgpa,
        }
        #print(new_js)
        arr_data.append(new_js)
        #input("...")
    n=n+1
dfn=pd.DataFrame(arr_data)
dfn.to_csv("finalresults.csv",index=False)