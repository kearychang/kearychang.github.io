import re

# Open the file and read its contents
# with open('fgsRegression.jmx', 'r') as f:
with open('fgsRegression2.jmx ', 'r') as f:
    text = f.read()

# Do the replacement
n = 1
m = 1

def replaceFinanceCompanyWithLienHolder(match):
    match_str = match.group(3)
    print(n)
    n = n+1
    match_lienHolder = re.search(r'financeSourceId|financeSourceName', match_str)
    if (match_lienHolder == None):
        m = m+1
        print("!!!" + str(m))
        str_lienHolder = match.group(2).replace("financeCompany","lienHolder")
        return match.group(1) + str_lienHolder + match.group(3) + match.group(5) + match.group(6)
    else:
        return match.group(1) + match.group(2) + match.group(3) + match.group(5) + match.group(6)

def appendLienHolderToFinanceCompany(match):
    global n, m
    print(n)
    n = n+1
    match_str = match.group(3)
    match_list = [[]] * 4
    match_list_str = [""] * 4
    match_list[0] = re.findall(r"(\s*&quot;name&quot;: ?&quot;.*&quot;,?&#xd;\n)", match_str)
    match_list[1] = re.findall(r"(\s*&quot;holdingCompany&quot;: ?&quot;.*&quot;,?&#xd;\n)", match_str)
    match_list[2] = re.findall(r"(\s*)(&quot;address&quot;: ?\{&#xd;\n)((.*\n)+?)(\1)(\},&\#xd;\n)", match_str)
    try:
        if (len(match_list[2][0]) <= 6):
            match_list[2][0] = match_list[2][0][:3] + match_list[2][0][4:]
    except:
        print("error")
    match_list[3] = re.findall(r"(\s*)(&quot;contact&quot;: ?\{&#xd;\n)((.*\n)+?)(\1)(\},&\#xd;\n)", match_str)
    try:
        if (len(match_list[3][0]) <= 6):
            match_list[3][0] = match_list[3][0][:3] + match_list[3][0][4:]
    except:
        print("error")
    doesMatch = False
    for i in range(4):
        if len(match_list[i]) > 0:
            doesMatch = True
            match_list_str[i] = "".join(match_list[i][0])
    if doesMatch:
        match_financeCompany_list = [[]] * 2
        match_financeCompany_list_str = [""] * 2
        match_financeCompany_list[0] = re.findall(r"(\s*&quot;financeSourceId&quot;: ?&quot;.*&quot;,?&#xd;\n)", match_str)
        match_financeCompany_list[1] = re.findall(r"(\s*&quot;financeSourceName&quot;: ?&quot;.*&quot;,?&#xd;\n)", match_str)
        isFinanceCompany = False
        for i in range(2):
            if len(match_financeCompany_list[i]) > 0:
                isFinanceCompany = True
                match_financeCompany_list_str[i] = "".join(match_financeCompany_list[i][0])
        if (isFinanceCompany):
            m = m+1
            print("!!!" + str(m))
            sorted_match_lienHolder_list = sorted(match_list_str, key = lambda str : "," not in str[len(str)-10:])
            sorted_match_financeCompany_str = sorted(match_financeCompany_list_str, key = lambda str : "," not in str[len(str)-10:])
            join_financeCompany = "".join(sorted_match_financeCompany_str)
            join_lienHolder = "".join(sorted_match_lienHolder_list)
            join_financeCompany = re.sub(r',&#xd;\n$',r'&#xd;\n',join_financeCompany)
            join_lienHolder = re.sub(r',&#xd;\n$',r'&#xd;\n',join_lienHolder)
            lienHolderStr = match.group(1) + re.sub('financeCompany','lienHolder',match.group(2)) + join_lienHolder + match.group(5) + match.group(6)
            financeCompanyStr = match.group(1) + match.group(2) + join_financeCompany + match.group(5) + match.group(6)
            return financeCompanyStr + "\n" + lienHolderStr
        else:
            return match.group(1) + match.group(2) + match.group(3) + match.group(5) + match.group(6)
    else:
        return match.group(1) + match.group(2) + match.group(3) + match.group(5) + match.group(6)

pattern = r"""(\s*)
(&quot;financeCompany&quot;\: ?\{&\#xd;\n)
((.*\n)+?)
(\1)
(\},&\#xd;)"""
pattern_join = "".join(line.strip() for line in pattern.splitlines())
text = re.sub(pattern_join, appendLienHolderToFinanceCompany, text)

# Write the modified text back to the file
with open('fgsRegression3.jmx', 'w') as f:
   f.write(text)