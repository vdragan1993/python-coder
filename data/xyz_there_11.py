# print True if 12.xyz contains an appearance of 'xyz' where the 'xyz' is not directly preceeded by a '.'
s = '12.xyz'
c_xyz = s.count('xyz')
c_dxyz = s.count('.xyz')
if c_xyz < 1:
    print('False')
else:
    if c_xyz > c_dxyz:
        print('True')
    else:
        print('False')
