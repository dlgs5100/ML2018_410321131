# NDHU 2018 Machine learning assignment1

## Instruction

>Encryption formula: </br>
𝐸 = 𝑤1𝐾1 + 𝑤2𝐾2 + 𝑤3𝐼 </br>

>Decryption formula: </br>
𝐼 = (𝐸 − w1𝐾1 − 𝑤2𝐾2) / 𝑤3 </br>

**Coefficient of w (w1,w2,w3)** </br>
𝐰 = [𝑤1, 𝑤2, 𝑤3] </br>
**Image Key1 (𝐾1)** </br>
![](Image/K1.JPG) </br>
**Image Key2 (𝐾2)** </br>
![](Image/K2.JPG) </br>
**Image be encrypted (𝐼)** </br>
![](Image/I.JPG) </br>
**Encrypted image (𝐸)** </br>
![](Image/E.JPG) </br>
![](Image/Formula.JPG) </br>

## Algorithm </br>
![](Image/Algorithm.JPG) </br>

## Experiment result </br>
**Initial 𝐰** </br>
w = [0,0,0] </br>
**Learning rate** </br>
𝛼 = 1e-5~1e-8 </br>
**Result 𝐰** </br>
w = [0.2491433070972368, 0.6613819010415319, 0.08923952571665969]] </br>
**Eprime** </br>
![](Image/Eprime.JPG) </br>
**Decryption_Eprime** </br>
![](Image/Decryption_Eprime.JPG) </br>

## Discussion </br>
實驗W初始值並不會造成劇烈影響 </br>
因此將之設置為0 </br>
當Learning rate低於1e-8時 </br>
需要Epoch>=4次才能找出合適的W並解譯出清晰Decryption_Eprime </br>
![](Image/Decryption_Eprime_Noise.JPG) </br>
