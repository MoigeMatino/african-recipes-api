<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

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

    public function creator(): BelongsTo
    {
        return $this->belongsTo(User::class, 'user_id');
    }

    public function tags(): BelongsToMany
    {
        return $this->belongsToMany(Tag::class, 'recipe_tag', 'recipe_id', 'tag_id')->withTimestamps();
    }

    public function likes(): int
    {
        return $this->belongsToMany(User::class, 'likes', 'recipe_id', 'user_id')->count('id')->withTimestamps();
    }

    public function users_liked(): BelongsToMany
    {
        return $this->belongsToMany(User::class, 'likes', 'recipe_id', 'user_id')->withTimestamps();
    }

    public function rating(): int //Todo: Confirm this actually works
    {
        return $this->belongsToMany(User::class, 'ratings', 'recipe_id', 'user_id')->withTimestamps()->withPivot('rating')->get()->avg('pivot.rating');
    }

    public function user_ratings(): BelongsToMany
    {
        return $this->belongsToMany(User::class, 'ratings', 'recipe_id', 'user_id')->withTimestamps();
    }

    public function collaborators(): BelongsToMany
    {
        return $this->belongsToMany(User::class, 'collaborators', 'user_id', 'recipe_id')->withTimestamps();
    }
}
