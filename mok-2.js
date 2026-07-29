function moktwo(plainText) {
    let LOC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    let keyText = 26;
    let saltText = 11;
    let Hblock = []
    for (let n = 0; n < 32; n++) {Hblock.push(keyText)};
    for (let i = 0; i < plainText.length; i++) {
        let char = plainText[i];
        let charind = LOC.indexOf(char);
        if (charind <= -1) { charind = saltText; };
        for (let j = 0; j < Hblock.length; j++) {
            Hblock[j] = ((Hblock[j] - charind) * -(i + (j + 1)) * keyText) % LOC.length;
            Hblock[j] ^= ((Hblock[(j + 2) % Hblock.length] << ((0x314159265 % (j + 1)) % 5)) & 0x314159265);
            Hblock[j] = Math.abs(Hblock[j]) % LOC.length;
        }
    }
    return Hblock.map(function(idx) { return LOC[idx]; }).join('');
}