class HelloWorld {
    public static void main(String[] args) {
        String key = "kcgcdfccb";
        String original = "";
        String Cipher = "Lg ccud qh urg tgay ejbwdkt, wmgtf su bgud nkudnk lrd vjfbg. Yrhfm qvd vng sfuuxytj \"vkj_ecwo_ogp_ej_rnfkukf\" wt iq urtuwjm. Ocz iqa jdag vio uzthsivi pqx vkj pgyd encpggt. Uy hopg yjg fhkz arz hkscv ckoq pgfn vu wwygt nkioe zttft djkth.";
        String cipher = Cipher.toLowerCase();
        String s = cipher.replaceAll(" ", "").replaceAll("_","").replaceAll(",","").replaceAll("\"","").replaceAll("\\.", "");
        int n= s.length();
        for(int i =0; i<n ; i++){
            int k=(s.charAt(i) -key.charAt(i%(key.length()))+26)% 26;
            k+='a';
            original+=(char)k;
        }
        System.out.println(original);
    }
}