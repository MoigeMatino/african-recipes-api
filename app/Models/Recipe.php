<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Recipe extends Model
{
    use HasFactory;

    protected $fillable = [
        'user_id',
        'title',
        'description',
        'instructions',
        'prep_time',
        'cook_time',
        'total_time',
        'servings',
        'image_url',
        'ingredients',
        'nutritional_info',
        'premium',
        'created_at',
        'updated_at',
    ];

    public function users{
        returns $this->belongsTo(User::class, 'user_id')
    }

    public function collaborators{
        // return $this->hasMany
    }
}
