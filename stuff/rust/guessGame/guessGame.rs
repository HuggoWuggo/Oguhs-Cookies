// By Hugo Lewczak
use std::cmp::Ordering;
use std::io;
use rand::Rng;

fn generate_num() -> u32 {
    let rng = rand::thread_rng().gen_range(1..101);
    rng
}

fn main() {
    let num:u32 = generate_num();
    println!("{}", num);
    loop {
        let mut guess = String::new();
        println!("Enter your guess: ");
        io::stdin().read_line(&mut guess).expect("Failed to read line");
        let guess:u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        match guess.cmp(&num) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }


}