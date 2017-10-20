def lindenmayer(frm, production_rules,nb_transf=1):
    if nb_transf < 1:
        return frm
    transformed = ''.join(production_rules.get(c, c) for c in frm)
    if nb_transf == 1:
        return transformed
    return lindenmayer(transformed, production_rules, nb_transf - 1)

    return 
if __name__ == "__main__":
    hilb = lindenmayer('L', {'L':'+RF-LFL-FR+', 'R':'-LF+RFR+FL-'}, 2)
    print(hilb)
    koch = lindenmayer('F', {'F':'F+F-F-F+F'},2)
    print(koch)
