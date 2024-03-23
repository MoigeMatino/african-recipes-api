<?php

namespace Database\Seeders;

use App\Models\User;
// use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     */
    public function run(): void
    {
        // https://fakerphp.github.io/

        // Seed Users
        $users = [
            "Lewis Munyi" => 'lewis@email.com',
            "Agatha Bahati" => 'agatha@email.com'
        ];

        foreach ($users as $key => $value) {
            User::create([
                'name' => $key,
                'email' => $value,
                'password' => bcrypt('secret')
            ]);
        }

        $this->call([UserSeeder::class]);
    }
}
