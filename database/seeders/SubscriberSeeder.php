<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Subscriber;

class SubscriberSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        for ($i = 0; $i < 1000; $i++) {
            $email = fake()->safeemail;
            Subscriber::updateOrCreate(
                [
                    'email' => $email,
                ],
                [
                    'name' => fake()->name,
                    'email' => $email
                ]
            );
        }
    }
}
