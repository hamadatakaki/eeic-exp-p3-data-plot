def safe_dictionary_access(dic, query, failval, warning=True):
    d = dic
    for q in query:
        cond_dic = type(d) == dict and type(q) in [int, str] and q in d
        cond_list = type(d) == list and type(q) == int and q < len(d) and q >= -len(d)

        if not (cond_dic or cond_list):
            if warning:
                print("[warn] the safe_dictionary_access query failed.")

                import pprint

                def _conv_q(q):
                    return f'"{q}"' if type(q) == str else str(q)

                query_str = ", ".join(map(_conv_q, query))
                print("  query:", q)
                print("  d-val:", d)
                print(f"  queries: `{query_str}`")
                print(f"  dictionary: {pprint.pformat(dic)}")

            return failval
        else:
            d = d[q]

    return d


def none_wrap(x, y):
    return x if x is not None else y


if __name__ == "__main__":
    dic = {"hoge": ["a", "b", {"c": 42}]}
    print(safe_dictionary_access(dic, ["hoge", 2, 2], -1))
