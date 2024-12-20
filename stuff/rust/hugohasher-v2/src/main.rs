// By Hugo Lewczak

use std::collections::HashMap;
use std::{env, fs};

#[derive(Debug)]
struct FLAGS {
    decrypt: bool,
    encrypt: bool,
    string: String,

    piped: bool,
    piped_file: String,

    file: bool,
    file_path: String,

    help: bool,
}

impl FLAGS {
    fn init() -> Self {
        FLAGS {
            decrypt: false,
            encrypt: false,
            string: String::new(),

            piped: false,
            piped_file: String::new(),

            file: false,
            file_path: String::new(),
            help: false,
        }
    }
}

fn main() {
    let mut flags = FLAGS::init();
    collect_args(&mut flags);

    //println!("{:?}", flags);

    if flags.help == false {
        if flags.decrypt == true && flags.encrypt == true {
            panic!("You cannot specify both -e and -d. Please choose either -e or -d.");
        } else if flags.encrypt == true {
            let mut encrypted = encrypt(flags.string.as_str(), basic_encryption_table());
            if flags.file == true {
                let contents = read_from_file(&flags);
                encrypted = encrypt(contents.as_str(), basic_encryption_table());
            }
            if flags.piped == true {
                write_to_file(flags, encrypted);
            } else {
                println!("Encrypted: {}", encrypted);
            }
        } else if flags.decrypt == true {
            let mut decrypted = decrypt(flags.string.as_str(), basic_encryption_table());
            if flags.file == true {
                let contents = read_from_file(&flags);
                decrypted = decrypt(&contents, basic_encryption_table());
            }
            if flags.piped == true {
                write_to_file(flags, decrypted.clone());
            } else {
                println!("Decrypted: {}", decrypted);
            }
        } else {
            panic!("You must specify either -e or -d to encrypt or decrypt the string.");
        }
    } else {
        println!(
            "
        WELCOME TO HUGOHASHER V2.0\n
        USAGE:
        * Represent required arguments
            -d* = decrypt file
            -e* = encrypt file
            -s = specify string to encrypt/decrypt
            -f = specify input file
            -o = specify output file
            -h = show this message

        EXAMPLES:
        hugohasher -e -s 'hello world' -o encrypted.txt

        hugohasher -d -f encrypted.txt -o decrypted.txt
            "
        )
    }
}

fn basic_encryption_table() -> HashMap<char, char> {
    let mut table: HashMap<char, char> = HashMap::new();

    for letter in 'a'..='z' {
        let next = if letter == 'z' {
            'a'
        } else {
            (letter as u8 + 1) as char
        };
        table.insert(letter, next);
    }

    table
}

fn collect_args(flags: &mut FLAGS) {
    let args: Vec<String> = env::args().collect();

    for (i, arg) in args.iter().enumerate() {
        match arg.as_str() {
            "-d" => flags.decrypt = true,
            "-e" => flags.encrypt = true,
            "-s" => flags.string = String::from(args[i + 1].clone()),
            "-f" => {
                flags.file = true;
                flags.file_path = String::from(args[i + 1].clone());
            }
            "-o" => {
                flags.piped = true;
                flags.piped_file = String::from(args[i + 1].clone());
            }
            "-h" => {
                flags.help = true;
            }
            _ => {
                if (i != 0) && (args[i - 1] != "-s" && args[i - 1] != "-f" && args[i - 1] != "-o") {
                    panic!("Unknown argument: {}", arg);
                }
            }
        }
    }
}

fn write_to_file(flags: FLAGS, contents: String) {
    let _can_write = fs::write(flags.piped_file, contents);
}

fn read_from_file(flags: &FLAGS) -> String {
    let read = fs::read_to_string(&flags.file_path).unwrap();
    read.to_string()
}

fn encrypt(src: &str, table: HashMap<char, char>) -> String {
    src.chars()
        .map(|letter| {
            if letter.is_alphabetic() {
                let lower_letter = letter.to_lowercase().next().unwrap();
                *table.get(&lower_letter).unwrap_or(&letter)
            } else {
                letter
            }
        })
        .rev()
        .collect()
}

fn decrypt(src: &str, table: HashMap<char, char>) -> String {
    let r_table: HashMap<char, char> = table.iter().map(|(&k, &v)| (v, k)).collect();

    src.chars()
        .rev()
        .map(|letter| {
            if letter.is_alphabetic() {
                *r_table.get(&letter).unwrap_or(&letter)
            } else {
                letter
            }
        })
        .collect()
}
