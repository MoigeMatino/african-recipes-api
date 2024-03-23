<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class UserSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
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

        for ($i = 0; $i < 10; $i++) {
            User::create([
                "name" => fake()->name,
                "email" => fake()->email,
                "password" => fake()->password,
            ]);
        }
    }
}
