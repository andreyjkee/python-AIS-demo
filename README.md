# python-AIS-demo
```
Begin Artificial Immune System for Intrusion Detection demo
Loading self-antigen set (normal historical patterns)
0: 1 0 0 1 0 1 1 0 1 0 0 1
1: 1 1 0 0 1 0 1 0 1 1 0 0
2: 1 0 1 1 0 0 1 1 0 1 0 1

3: 0 0 1 1 0 1 0 1 1 0 1 1
4: 0 1 0 1 0 1 0 0 1 1 0 1
5: 0 0 1 0 1 0 1 0 0 1 0 0
Creating lymphocyte set using negative selection and r-chunks detection
0: antibody = 1 1 1 1 age = 0 stimulation = 0
1: antibody = 1 0 0 0 age = 0 stimulation = 0
2: antibody = 0 1 1 1 age = 0 stimulation = 0
Begin AIS intrusion detection simulation
===============================================
Incoming pattern = 0 0 0 1 1 1 1 1 1 1 1 0
Incoming pattern detected by lymphocyte 0
Lymphocyte 0 not over stimulation threshold
Incoming pattern not detected by lymphocyte 1
Incoming pattern detected by lymphocyte 2
Lymphocyte 2 not over stimulation threshold
===============================================
===============================================
Incoming pattern = 1 1 1 1 0 1 1 0 0 0 0 0
Incoming pattern detected by lymphocyte 0
Lymphocyte 0 not over stimulation threshold
Incoming pattern detected by lymphocyte 1
Lymphocyte 1 not over stimulation threshold
Incoming pattern not detected by lymphocyte 2
===============================================
===============================================
Incoming pattern = 1 1 1 1 1 0 1 0 1 1 1 0
Incoming pattern detected by lymphocyte 0
Lymphocyte 0 stimulated! Check incoming as possible intrusion!
Incoming pattern not detected by lymphocyte 1
Incoming pattern detected by lymphocyte 2
Lymphocyte 2 not over stimulation threshold
===============================================
===============================================
Incoming pattern = 0 0 1 0 0 1 1 1 1 0 0 0
Incoming pattern detected by lymphocyte 0
Lymphocyte 0 stimulated! Check incoming as possible intrusion!
Incoming pattern detected by lymphocyte 1
Lymphocyte 1 not over stimulation threshold
Incoming pattern detected by lymphocyte 2
Lymphocyte 2 stimulated! Check incoming as possible intrusion!
===============================================
===============================================
Incoming pattern = 0 0 1 0 1 0 1 1 0 1 1 1
Incoming pattern not detected by lymphocyte 0
Incoming pattern not detected by lymphocyte 1
Incoming pattern detected by lymphocyte 2
Lymphocyte 2 stimulated! Check incoming as possible intrusion!
===============================================
===============================================
Incoming pattern = 1 0 1 1 0 1 0 0 0 1 0 0
Incoming pattern not detected by lymphocyte 0
Incoming pattern detected by lymphocyte 1
Lymphocyte 1 stimulated! Check incoming as possible intrusion!

Incoming pattern not detected by lymphocyte 2
===============================================
End of AIS demo
```
