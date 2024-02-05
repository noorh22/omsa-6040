# NOTEBOOK 4 - FLOATING POINT
# PART 0

def eval_strint(s, base=2):
    assert type(s) is str
    assert 2 <= base <= 36
    return int(s, base)


# print(f"eval_strint('6040', 8) -> {eval_strint('6040', 8)}")
# print(f"eval_strint('deadbeef', 16) -> {eval_strint('deadbeef', 16)}")
# print(f"eval_strint('4321', 5) -> {eval_strint('4321', 5)}")


dict = {str(i): i for i in range(10)}
for index, char in enumerate('abcdefghijklmnopqrstuvwxyz', 10):
    dict[char] = index


# print(dict)


def eval_strfrac(s, base=2):
    point_sep = s.split('.')
    int_val = eval_strint(point_sep[0], base)
    added_dec = 0
    if len(point_sep) == 2:
        for count, val in enumerate(point_sep[1], 1):
            added_dec += dict[val] * (base ** (-count))

    final_sum = added_dec + float(int_val)
    return final_sum


# print(f"eval_strfrac('3.14', base=10) -> {eval_strfrac('3.14', base=10)}")
# print(f"eval_strfrac('100.101', base=2) -> {eval_strfrac('100.101', base=2)}")
# print(f"eval_strfrac('2c', base=16) -> {eval_strfrac('2c', base=16)}")


def fp_bin(v):
    assert type(v) is float
    v_hex = v.hex()
    if v >= 0:
        s_sign = '+'
    else:
        s_sign = '-'

    print(s_sign)
    string_split = v_hex.split('p')
    v_exp = int(string_split[1])
    hex_dec = int((v_hex[v_hex.index('.') + 1:v_hex.index('p')]), 16)
    bin_num = str(bin(hex_dec))[2:]
    print(len(bin_num))
    if len(bin_num) < 52:
        diff = 52 - len(bin_num)
        zero_str = "0" * diff
    else:
        zero_str = ""

    result = (s_sign, v_hex.split('.')[0][-1] + "." + zero_str + bin_num, v_exp)
    print(result)
    return result


v = -1280.03125
print(v.hex())
fp_bin(v)


def eval_fp(sign, significand, exponent, base=2):
    assert sign in ['+', '-'], "Sign bit must be '+' or '-', not '{}'.".format(sign)
    assert type(exponent) is int
    lower_sig = significand.lower()
    sig_float = eval_strfrac(lower_sig, base)
    if sign == '-':
        float_sign = -1
    else:
        float_sign = 1
    end_result = float_sign * sig_float * (base ** exponent)
    return end_result


def add_fp_bin(u, v, signif_bits):
    u_sign, u_signif, u_exp = u
    v_sign, v_signif, v_exp = v
    # You may assume normalized inputs at the given precision, `signif_bits`.
    assert u_signif[:2] in {'1.', '0.'} and len(u_signif) == (signif_bits + 1)
    assert v_signif[:2] in {'1.', '0.'} and len(v_signif) == (signif_bits + 1)
    u_int = eval_fp(u[0], u[1], u[2], 2)
    print(u_int)
    v_int = eval_fp(v[0], v[1], v[2], 2)
    print(v_int)
    uv_sum = u_int + v_int
    print(uv_sum)
    uv_bin = fp_bin(uv_sum)
    sig_bits = uv_bin[1][:signif_bits + 1]
    return (uv_bin[0], sig_bits, uv_bin[2])


u = ('+', '1.010010', 0)
v = ('-', '1.000000', -2)
assert add_fp_bin(u, v, 7) == ('+', '1.000010', 0)

# PART 1
# Excercise 0
def alg_sum(x): # x == x[:n]
    s = 0.
    for x_i in x: # x_0, x_1, \ldots, x_{n-1}
        s += x_i
    return s


N = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
# Initialize an array t of size len(N) to all zeroes.
t = [0.0] * len(N)

for i in range(len(N)):
    x = [0.1 * N[i]]
    r = alg_sum(x)
    print(r)
    t[i] = r

print(t)

#Excercise 2

def alg_sum_accurate(nums):
    assert type(nums) is list
    partials = []  # sorted, non-overlapping partial sums
    for x in nums:
        i = 0
        for y in partials:
            if abs(x) < abs(y):
                x, y = y, x
            hi = x + y
            lo = y - (hi - x)
            if lo:
                partials[i] = lo
                i += 1
            x = hi
        partials[i:] = [x]
    return sum(partials, 0.0)
